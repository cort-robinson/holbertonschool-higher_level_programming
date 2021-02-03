#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2).sort(function (a, b) { return a - b; });
  console.log(Number(nums[nums.length - 2]));
}
