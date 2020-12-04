"""全排列的问题"""
# 初始化返回结果
res = []


# 主函数
def main(nums):
    track = []
    backtrack(nums, track)
    return res


# 回溯函数
# nums是一组不重复的数（输入）
# track是路径
def backtrack(nums, track):
    # 触发结束条件
    if len(nums) == len(track):
        res.append(track[:])
        return

    # 开始遍历树
    for i in range(len(nums)):
        # 排除不合法的选择
        if nums[i] in track:
            continue
        # 做选择
        track.append(nums[i])
        # 进入下一层决策树
        backtrack(nums, track)
        # 删除选择
        track.pop()

