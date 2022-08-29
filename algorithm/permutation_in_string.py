class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only passed test cases with len(s1)==2
        if (len(s1)>len(s2)):
            temp = s1
            s1 = s2
            s2 = temp
        
        s1_rev = "".join(list(s1)[::-1])
        print(s1_rev)
        l, r = 0, len(s2)-1
        
        while (l < r):
            if (s2[l:r+1]==s1):
                return True
            elif (s2[l]==s1[0]):
                r -= 1
            else:
                l += 1
        l, r = 0, len(s2)-1
        while (l < r):
            if (s2[l:r+1]==s1_rev):
                return True
            elif (s2[l]==s1_rev[0]):
                r -= 1
            else:
                l += 1

        return False


        # slid window
        # s2 is having the same number of characters as in the s1
        # create a hashmap with the count of every character in the string s1.
        # Then we slide a window over the string s2 and decrease the counter for characters that occurred in the window.
        # As soon as all counters in the hashmap get to zero that means we encountered the permutation.
        # Time: O(n) - linear for window sliding and counter
        # Space: O(1) - conctant for dictionary with the maximum 26 pairs (English alphabet)
        cntr, w, match = Counter(s1), len(s1), 0     

        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]: match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]: match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]: match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]: match += 1

            if match == len(cntr):
                return True

        return False


        # array
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False


        # sorting
        if s2 and not s1:
            return True
        '''
        --1--
        [Accepted]
        [Runtime: 9408 ms, faster than 5.07%]
        
        One string is a permutation of another if 
        they are the same string when sorted. 
        
        Hence, sort s1 and then sort the substrings of s2 that are of the same size
        and compare
        Time: O(n)*O(k^2)*O(klogk) = O(n*k^3*logk)
        '''
        
        # sort s1
        s1 = "".join(sorted(list(s1)))
        k = len(s1)
    
        # sort the substrings of s2 that are of the same size
        for i in range(len(s2)): # -- O(n)
            sub = s2[i:i+k] # -- O(k)
            sub_str = "".join(sorted(list(sub)))  # ---- [1] 
        
            if s1 == sub_str:
                return True
        return False
    
        # COMMENT [1]:
        # ------------
        # Runtime of that line = O(klogk) * O(k) * O(K)
        # Sorting and converting from string to list and back into a string


        # hashtable
        '''
       --2--
       [Accepted]
       [Runtime: 3556 ms, faster than 5.07% ]
       
       One string is a permutation of another if the two strings
       have the same character frequencies
       
       Hence:
           - find freq dict for s1
           - find freq dict for substrings of s2 (that are the same size as s1)
           
       runtime: O(n*k^2)
       '''
       
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False


        # rolling hash
        '''
        --3--
        [Accepted]
        [Runtime: 72 ms, faster than 57.45%]
        
        Enhanced freq dict - (Rolling hashmap)
        simiar problem: 438. Find All Anagrams in a String
        
            - instead of generating a fresh freq hashmap for every new substring
            - build the freq dict for the initial window and then slide the window_dict
              (add/remove chars) by adjusting their frequinces. 
              
              removing one preceding character and adding a new succeeding character to the new window
        '''
        
        k = len(s1)
        from collections import Counter
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        d2 = Counter(window)
        
        # check the intial window 
        if d1 == d2:
            return True
  
        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
                
        return False

# brute force
# o do so, permute takes the index of the current element current\_indexcurrent_index as one of the arguments.
# Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements.
# After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array.
# While returning back, we reverse the swapping done in the current function call.

# Thus, when we reach the end of the array, a new ordering of the array's elements is generated. 
# Time complexity: O(n!)O(n!).
# Space complexity: O(n^2). The depth of the recursion tree is n(n refers to the length of the short string s1).
# Every node of the recursion tree contains a string of max. length n.
# public class Solution {
#     boolean flag = false;
    
#     public boolean checkInclusion(String s1, String s2) {
#         permute(s1, s2, 0);
#         return flag;
#     }
    
#     public String swap(String s, int i0, int i1) {
#         if (i0 == i1)
#             return s;
#         String s1 = s.substring(0, i0);
#         String s2 = s.substring(i0 + 1, i1);
#         String s3 = s.substring(i1 + 1);
#         return s1 + s.charAt(i1) + s2 + s.charAt(i0) + s3;
#     }
    
#     void permute(String s1, String s2, int l) {
#         if (l == s1.length()) {
#             if (s2.indexOf(s1) >= 0)
#                 flag = true;
#         } else {
#             for (int i = l; i < s1.length(); i++) {
#                 s1 = swap(s1, l, i);
#                 permute(s1, s2, l + 1);
#                 s1 = swap(s1, l, i);
#             }
#         }
#     }
# }

# sorting
# one string will be a permutation of another string only if both of them contain the same characters the same number of times.
# sorted(x)=sorted(y)
# Let l_1be the length of string s_1and l_2be the length of string s_2.
# Time complexity: O(l_1log(l_1)+(l_2−l_1)l_1log(l_1)).
# Space complexity: O(l_1). t array is used.
# time complexity: O()
# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         s1 = sort(s1);
#         for (int i = 0; i <= s2.length() - s1.length(); i++) {
#             if (s1.equals(sort(s2.substring(i, i + s1.length()))))
#                 return true;
#         }
#         return false;
#     }
    
#     public String sort(String s) {
#         char[] t = s.toCharArray();
#         Arrays.sort(t);
#         return new String(t);
#     }
# }

# hashmap
# consider every possible substring in the long string s2s2 of the same length as that of s1s1 and check the frequency of occurence of the characters appearing in the two
# make use of a hashmap s1map which stores the frequency of occurence of all the characters in the short string s1
# consider every possible substring of s2 of the same length as that of s1s1, find its corresponding hashmap as well
# Let l_1 be the length of string s_1 and l_2 be the length of string s_2.
# Time complexity: O(l_1+26l_1(l_2-l_1)). The hashmap contains atmost 26 keys.
# Space complexity: O(1). Hashmap contains at most 26 key-value pairs.


# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         if (s1.length() > s2.length())
#             return false;
#         HashMap<Character, Integer> s1map = new HashMap<>();

#         for (int i = 0; i < s1.length(); i++)
#             s1map.put(s1.charAt(i), s1map.getOrDefault(s1.charAt(i), 0) + 1);

#         for (int i = 0; i <= s2.length() - s1.length(); i++) {
#             HashMap<Character, Integer> s2map = new HashMap<>();
#             for (int j = 0; j < s1.length(); j++) {
#                 s2map.put(s2.charAt(i + j), s2map.getOrDefault(s2.charAt(i + j), 0) + 1);
#             }
#             if (matches(s1map, s2map))
#                 return true;
#         }
#         return false;
#     }

#     public boolean matches(HashMap<Character, Integer> s1map, HashMap<Character, Integer> s2map) {
#         for (char key : s1map.keySet()) {
#             if (s1map.get(key) - s2map.getOrDefault(key, -1) != 0)
#                 return false;
#         }
#         return true;
#     }
# }


# array
# store the frequencies
# take an array of size 26.The rest of the process remains the same as the last approach.
# Let l_1 be the length of string s_1 and l_2 be the length of string s_2.
# Time complexity: O(l_1+26l_1(l_2-l_1)).
# Space complexity: O(1). s1map and s2map of size 26 is used.
# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         if (s1.length() > s2.length())
#             return false;
#         int[] s1map = new int[26];
#         for (int i = 0; i < s1.length(); i++)
#             s1map[s1.charAt(i) - 'a']++;
#         for (int i = 0; i <= s2.length() - s1.length(); i++) {
#             int[] s2map = new int[26];
#             for (int j = 0; j < s1.length(); j++) {
#                 s2map[s2.charAt(i + j) - 'a']++;
#             }
#             if (matches(s1map, s2map))
#                 return true;
#         }
#         return false;
#     }
    
#     public boolean matches(int[] s1map, int[] s2map) {
#         for (int i = 0; i < 26; i++) {
#             if (s1map[i] != s2map[i])
#                 return false;
#         }
#         return true;
#     }
# }

# sliding window
# create the hashmap just once for the first window in s2.
# update the hashmap by just updating the indices associated with those two characters only
# Let l_1 be the length of string s_1 and l_2 be the length of string s_2.
# Time complexity: O(l_1+26*(l_2-l_1)).
# Space complexity: O(1). Constant space is used.
# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         if (s1.length() > s2.length())
#             return false;
#         int[] s1map = new int[26];
#         int[] s2map = new int[26];
#         for (int i = 0; i < s1.length(); i++) {
#             s1map[s1.charAt(i) - 'a']++;
#             s2map[s2.charAt(i) - 'a']++;
#         }
#         for (int i = 0; i < s2.length() - s1.length(); i++) {
#             if (matches(s1map, s2map))
#                 return true;
#             s2map[s2.charAt(i + s1.length()) - 'a']++;
#             s2map[s2.charAt(i) - 'a']--;
#         }
#         return matches(s1map, s2map);
#     }
    
#     public boolean matches(int[] s1map, int[] s2map) {
#         for (int i = 0; i < 26; i++) {
#             if (s1map[i] != s2map[i])
#                 return false;
#         }
#         return true;
#     }
# }

# optiimised:
# keep a track of the number of elements which were already matching in the earlier hashmap and
# update just the count of matching elements when we shift the window towards the right.
# maintain a count variable, which stores the number of characters(out of the 26 alphabets): same frequency of occurence in s1 and the current window in s2.
# if the deduction of the last element and the addition of the new element leads to a new frequency match of any of the characters, we increment the countcount by 1.
# If not, we keep the countcount intact
# if a character whose frequency was the same earlier(prior to addition and removal) is added,
# it now leads to a frequency mismatch which is taken into account by decrementing the same countcount variable.
# If, after the shifting of the window, the countcount evaluates to 26,
# it means all the characters match in frequency totally. So, we return a True in that case immediately.
# Let l_1 be the length of string s_1 and l_2 be the length of string s_2.
# Time complexity: O(l_1+(l_2-l_1)).
# Space complexity: O(1). Constant space is used.
# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         if (s1.length() > s2.length())
#             return false;
#         int[] s1map = new int[26];
#         int[] s2map = new int[26];
#         for (int i = 0; i < s1.length(); i++) {
#             s1map[s1.charAt(i) - 'a']++;
#             s2map[s2.charAt(i) - 'a']++;
#         }

#         int count = 0;
#         for (int i = 0; i < 26; i++) {
#             if (s1map[i] == s2map[i])
#                 count++;
#         }

#         for (int i = 0; i < s2.length() - s1.length(); i++) {
#             int r = s2.charAt(i + s1.length()) - 'a', l = s2.charAt(i) - 'a';
#             if (count == 26)
#                 return true;
#             s2map[r]++;
#             if (s2map[r] == s1map[r]) {
#                 count++;
#             } else if (s2map[r] == s1map[r] + 1) {
#                 count--;
#             }
#             s2map[l]--;
#             if (s2map[l] == s1map[l]) {
#                 count++;
#             } else if (s2map[l] == s1map[l] - 1) {
#                 count--;
#             }
#         }
#         return count == 26;
#     }
# }