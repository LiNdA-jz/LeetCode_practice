# answers from bilibili
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        # len(x) == len(y) -> zip
        for x, y in zip(energy, experience):
            # both strictly greater experience and energy to defeat them and move to the next opponent if available
            if initialEnergy <= x:
                # training energy
                ans += x + 1 - initialEnergy
                initialEnergy = x + 1
            # decrease energy
            initialEnergy -= x

            if initialExperience <= y:
                # training experience
                ans += y + 1 - initialExperience
                initialExperience = y + 1
            # increase experience
            initialExperience += y

        return ans