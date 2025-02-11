class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Проверка на соответствие длинны строк
        if len(s) != len(t):
            return False

        # hashmap соответствия элементов s и t
        map_s_to_t = {}
        # Элементы, которые имеют hashmap в s
        mapped_in_t = []

        i = 0
        for i in range(len(s)):
            if s[i] not in map_s_to_t:
                if t[i] in mapped_in_t:
                    # Если ключу s[i] нет соответствия значения в t
                    # при этом для t[i] существует ключ в s[i]
                    return False
                # Если нет связи s[i] = t[i], то добавляем в словарь
                # и в список t[i]
                map_s_to_t[s[i]] = t[i]
                mapped_in_t.append(t[i])
            else:
                if map_s_to_t[s[i]] != t[i]:
                    # Если ключу s[i] есть соответствие значения в t
                    # и при этом оно не совпадает с текущим значением t[i]
                    return False
        return True