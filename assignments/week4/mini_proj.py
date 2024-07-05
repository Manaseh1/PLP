import json

#hii ni yakuloadin the json file
def load_def(json_file):
    with open(json_file, 'r') as f:
        defz = json.load(f)
    return defz

# checks if the word is in the file
def lookup_def(defz, word):
    if word in defz:
        return defz[word]
    else:
        return None

def main():
    json_file = 'data.json'
    defz = load_def(json_file)

    while True:
        # hii inafanya words zako zikuwe lowercase
        word = input("Enter a word to lookup (or 'q' to quit): ").strip().lower()
        #stops the search 
        if word == 'q':
            break
        
        defz = lookup_def(defz, word)
        
        if defz:
            print(f"Definition of '{word}':")
            for d in defz:
                print(f"- {d}")
        else:
            print(f"No definition found for '{word}'.")

if __name__ == "__main__":
    main()
