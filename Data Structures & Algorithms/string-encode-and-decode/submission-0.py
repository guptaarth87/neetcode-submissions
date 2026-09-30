

class Solution:
    def encodeSingleWord(self, word):
        encoded_word = ""
        for i in list(word):
            encoded_word += str(ord(i))+'/'
        return encoded_word

    def encode(self, strs: List[str]) -> str:
       final_encoded = ""
       for j in strs:
         
          final_encoded += self.encodeSingleWord(j) + "-"
       return final_encoded

    def decode(self, s: str) -> List[str]:
        final_list = []
        word = ""
        char_seq = ""
        for i in list(s):
            if i != "/" and i != "-":
                char_seq += i
            elif i == "/":
                integer_conv = int(char_seq)
                word += chr(integer_conv)
                char_seq = ""
                continue
            elif i == "-":
                final_list.append(word)
                word = ""

        return final_list
