class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        for i in range(m):
            image[i] = image[i][::-1]
            for j in range(n):
                image[i][j] = image[i][j] ^ 1
        return image
