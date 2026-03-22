# ============================================
#   Password Strength Checker
#   Beginner Cybersecurity Project
#   By: [Apna Naam Yahan Likho]
# ============================================

import re

# Terminal mein color ke liye
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def check_password(password):
    score = 0
    suggestions = []

    # ── 1. Length check ──────────────────────
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 15
        suggestions.append("📏 Password kam se kam 12 characters ka banao")
    else:
        suggestions.append("📏 Password bahut chota hai! 12+ characters use karo")

    # ── 2. Uppercase letters ─────────────────
    if re.search(r'[A-Z]', password):
        score += 20
    else:
        suggestions.append("🔠 Kam se kam ek Capital letter (A-Z) add karo")

    # ── 3. Lowercase letters ─────────────────
    if re.search(r'[a-z]', password):
        score += 20
    else:
        suggestions.append("🔡 Kam se kam ek small letter (a-z) add karo")

    # ── 4. Numbers ───────────────────────────
    if re.search(r'[0-9]', password):
        score += 15
    else:
        suggestions.append("🔢 Kam se kam ek number (0-9) add karo")

    # ── 5. Special characters ────────────────
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        score += 15
    else:
        suggestions.append("✨ Ek special character add karo jaise !@#$%")

    # ── 6. Common passwords check ────────────
    common = ["password", "123456", "qwerty", "abc123",
              "password1", "admin", "letmein", "welcome"]
    if password.lower() in common:
        score = 0
        suggestions = ["🚫 Yeh password bahut common hai! Bilkul mat use karo."]

    return score, suggestions


def get_strength_label(score):
    if score >= 90:
        return f"{GREEN}{BOLD}💪 BAHUT STRONG{RESET}", GREEN
    elif score >= 70:
        return f"{GREEN}✅ STRONG{RESET}", GREEN
    elif score >= 50:
        return f"{YELLOW}⚠️  MEDIUM{RESET}", YELLOW
    elif score >= 30:
        return f"{RED}❌ WEAK{RESET}", RED
    else:
        return f"{RED}{BOLD}☠️  BAHUT WEAK{RESET}", RED


def draw_progress_bar(score, color):
    filled = int(score / 5)       # 100 score = 20 blocks
    empty  = 20 - filled
    bar = color + "█" * filled + RESET + "░" * empty
    return f"[{bar}] {score}/100"


def main():
    print(f"\n{CYAN}{BOLD}{'='*45}")
    print("   🔐 Password Strength Checker")
    print(f"{'='*45}{RESET}\n")

    while True:
        password = input(f"{BOLD}Password enter karo (ya 'q' likhke exit karo): {RESET}")

        if password.lower() == 'q':
            print(f"\n{CYAN}👋 Alvida! Safe raho! 🔐{RESET}\n")
            break

        if not password:
            print(f"{RED}❌ Kuch toh likho!{RESET}\n")
            continue

        score, suggestions = check_password(password)
        label, color       = get_strength_label(score)
        bar                = draw_progress_bar(score, color)

        print(f"\n{BOLD}📊 Result:{RESET}")
        print(f"  Strength : {label}")
        print(f"  Score    : {bar}")

        if suggestions:
            print(f"\n{BOLD}💡 Suggestions:{RESET}")
            for s in suggestions:
                print(f"  {s}")
        else:
            print(f"\n{GREEN}🎉 Zabardast! Yeh ek perfect password hai!{RESET}")

        print(f"\n{'-'*45}\n")


if __name__ == "__main__":
    main()
