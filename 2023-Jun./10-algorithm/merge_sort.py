def merge(left, right):
  left_len = len(left)
  right_len = len(right)
  merged_data = [0] * (left_len + right_len) # [0,0,0,0]　みたいなのを作る
  print(merged_data)
  left_i, right_i, md_i = 0, 0, 0
  while left_i < left_len and right_i < right_len:
    if left[left_i] < right[right_i]:
      merged_data[md_i] = left[left_i]
      left_i += 1
    else:
      merged_data[md_i] = right[right_i]
      right_i += 1
    md_i += 1
  return merged_data[:md_i] + left[left_i:] + right[right_i:]

# print(merge([5, 8], [3, 7]))   # 「[3, 5, 7, 8]」を表示

def merge_sort(data):
  if len(data) <= 1: return data
  mid = len(data) // 2
  left_data = merge_sort(data[:mid])
  right_data = merge_sort(data[mid:])
  return merge(left_data, right_data)

data = [8,5,3,7,9,1,2,0]
print(merge_sort(data))