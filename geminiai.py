import google.generativeai as genai
import subprocess
from git import Repo
from datetime import datetime
import time
import os

# Konfigurasi API key untuk Gemini AI
genai.configure(api_key="AIzaSyC8VzKh1rDmrlcclDY44i12oANZ6zWY9mo")

# Mulai menghitung waktu untuk response speed
start_time = time.time()

# Menggunakan model 'gemini-1.5-flash' untuk generate kalimat
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Make a 2 paragraphs max about adventure in the medieval era (travel across land) or future era (travel between planets and galaxies).")

# Akhiri perhitungan waktu setelah response diterima
end_time = time.time()

# Hitung kecepatan respons dalam milidetik
response_speed_ms = int((end_time - start_time) * 1000)

# Ambil teks hasil generasi dari response
generated_text = response.text

# Dapatkan path dari direktori tempat script berada
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path untuk README.md di direktori yang sama dengan script
readme_path = os.path.join(script_dir, "README.md")

# Dapatkan tanggal saat ini
current_date = datetime.now().strftime("%d %B %Y")

# Menulis kalimat baru dan signature ke dalam README.md, menimpa isi sebelumnya
with open(readme_path, "w") as readme_file:  # Gunakan "w" untuk menimpa file
    readme_file.write(f"\n{generated_text}\n")  # Teks baru
    readme_file.write(f"~ By Hozmi - {current_date}\n")  # Signature dengan tanggal

# Dapatkan tanggal saat ini
current_date = datetime.now().strftime("%d %B %Y")

# Commit perubahan ke Git dan Push ke repository GitHub
commit_message = f"Update on {current_date} with response speed {response_speed_ms}ms"

git_repo_path = r'C:\Users\abdil\OneDrive\Documents\Project\Python\hozmi-adventure\.git'

def git_push():
    try:
        repo = Repo(git_repo_path)
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print(f'Some error occurred while pushing the code: {e}')    

git_push()
