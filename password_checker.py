
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
        suggestions.append("📏 Create password atleast 12+ character")
    else:
        suggestions.append("📏 Password is so small !  use Chracters 12+")

    # ── 2. Uppercase letters ─────────────────
    if re.search(r'[A-Z]', password):
        score += 20
    else:
        suggestions.append("🔠 Add atleast one capital letter ( A-Z) ")

    # ── 3. Lowercase letters ─────────────────
    if re.search(r'[a-z]', password):
        score += 20
    else:
        suggestions.append("🔡 Add atleast one small letter (a-z) ")

    # ── 4. Numbers ───────────────────────────
    if re.search(r'[0-9]', password):
        score += 15
    else:
        suggestions.append("🔢 Add atleast one number (0-9)")

    # ── 5. Special characters ────────────────
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        score += 15
    else:
        suggestions.append("✨ Add atleast one special character !@#$%")

    # ── 6. Common passwords check ────────────
    common = ["password", "123456", "qwerty", "abc123",
              "password1", "admin", "letmein", "welcome"]
    if password.lower() in common:
        score = 0
        suggestions = ["🚫 This password is too common! Do not use."]

    return score, suggestions


def get_strength_label(score):
    if score >= 90:
        return f"{GREEN}{BOLD}💪 TOO STRONG{RESET}", GREEN
    elif score >= 70:
        return f"{GREEN}✅ STRONG{RESET}", GREEN
    elif score >= 50:
        return f"{YELLOW}⚠️  MEDIUM{RESET}", YELLOW
    elif score >= 30:
        return f"{RED}❌ WEAK{RESET}", RED
    else:
        return f"{RED}{BOLD}☠️  VERy WEAK{RESET}", RED


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
        password = input(f"{BOLD}Enter the password (or enter 'q' to exit ): {RESET}")

        if password.lower() == 'q':
            print(f"\n{CYAN}👋 Bye! Be safe ! 🔐{RESET}\n")
            break

        if not password:
            print(f"{RED}❌ Wright Something!{RESET}\n")
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
            print(f"\n{GREEN}🎉 Woooww Very Nice! That is perfect password!{RESET}")

        print(f"\n{'-'*45}\n")


if __name__ == "__main__":
    main()
