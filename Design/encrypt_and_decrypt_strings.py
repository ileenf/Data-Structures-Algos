class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encrypted = dict()
        for i in range(len(keys)):
            self.encrypted[keys[i]] = values[i]
        
        self.decrypted = defaultdict(int)
        for word in dictionary:
            decrypt = self.encrypt(word)
            self.decrypted[decrypt] += 1
        
        
    def encrypt(self, word1: str) -> str:
        encrypted = []
        for ch in word1:
            if ch not in self.encrypted:
                return ''
            encrypted.append(self.encrypted[ch])
        return ''.join(encrypted)
        
    def decrypt(self, word2: str) -> int:
        return self.decrypted[word2]
