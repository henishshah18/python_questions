total_emails = int(input())
emails_with_free = int(input())
spam_emails = int(input())
spam_and_free = int(input())

if total_emails <= 0 or emails_with_free < 0 or spam_emails < 0 or spam_and_free < 0:
    print("Invalid input")
elif emails_with_free > total_emails or spam_emails > total_emails or spam_and_free > spam_emails or spam_and_free > emails_with_free:
    print("Invalid input")
else:
    p_spam = spam_emails / total_emails
    p_free = emails_with_free / total_emails
    p_free_given_spam = spam_and_free / spam_emails if spam_emails != 0 else 0
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free if p_free != 0 else 0
    print(f"P(Spam | Free): {p_spam_given_free:.4f}")
