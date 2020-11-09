n = int(input())
arr = map(int, input().split()) #mapping the splitted input into type int
print(sorted(list(set(arr)))[-2])
