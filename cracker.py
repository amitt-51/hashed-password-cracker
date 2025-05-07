import hashlib

def crack_hash(hash_value, wordlist_path, output_widget, hash_type):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line_number, line in enumerate(file, 1):
                password = line.strip()
                if not password:
                    continue

                # Hash the password using the specified hash type
                hashed = getattr(hashlib, hash_type)(password.encode()).hexdigest()

                if hashed == hash_value:
                    output_widget.insert("end", f"✅ Password Found: {password}\n")
                    return

    except FileNotFoundError:
        output_widget.insert("end", "⚠️ Wordlist file not found.\n")
        return
    except Exception as e:
        output_widget.insert("end", f"⚠️ Error reading wordlist: {e}\n")
        return

    output_widget.insert("end", "❌ Password not found.\n")

