import itertools
import random
import requests
import time

# الحروف والأرقام الممكنة
CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"

# عدد اليوزرات اللي تبغى تفحصها
SAMPLE_SIZE = 50

# طول اليوزرات (3 أو 4)
LENGTHS = [3, 4]

def generate_usernames(lengths, sample_size):
    """توليد عينة عشوائية من يوزرات ثلاثية ورباعية"""
    all_candidates = []
    for L in lengths:
        all_candidates.extend(
            ["".join(p) for p in itertools.product(CHARS, repeat=L)]
        )
    return random.sample(all_candidates, sample_size)

def check_username(username):
    """فحص إذا اليوزر متاح أو محجوز"""
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            return "متاح ✅"
        else:
            return "محجوز ❌"
    except:
        return "خطأ بالاتصال ⚠️"

def main():
    usernames = generate_usernames(LENGTHS, SAMPLE_SIZE)

    for i, u in enumerate(usernames, 1):
        status = check_username(u)
        print(f"[{i}/{len(usernames)}] {u} → {status}")
        time.sleep(0.5)  # تأخير بسيط لتجنب الحظر

if __name__ == "__main__":
    main()
