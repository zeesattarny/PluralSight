store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(store)
    return sorted(strings, key=last_letter)

if "__name__" == "__main__":
   sort_by_last_letter(['hello', 'from a', 'local function'])