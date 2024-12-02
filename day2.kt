import java.io.File
import kotlin.math.abs

fun day2part1(filename: String): Int {
    val file = File(filename)

    if (!file.exists()) {
        println("$filename does not exist")
        return -1
    }

    var safe = 0

    file.forEachLine { line -> 
        val nums = line.split("\\s+".toRegex()).map { it.toInt() }
        safe += if (isSafe(nums)) 1 else 0
    }

    return safe
}

fun isSafe(nums: List<Int>): Boolean {
    var lineIsSafe = true
    var increasing = false
    for (i in 1 until nums.size) {
        val diff = nums[i] - nums[i - 1]

        if (diff > 0 && i == 1) increasing = true
        else if (diff > 0 && !increasing) {
            lineIsSafe = false
            break
        }
        else if (diff < 0 && increasing) {
            lineIsSafe = false
            break
        }

        if (abs(diff) < 1 || abs(diff) > 3) {
            lineIsSafe = false
            break
        }
    }

    return lineIsSafe
}

fun day2part2(filename: String): Int {
    val file = File(filename)

    if (!file.exists()) {
        println("$filename does not exist")
        return -1
    }

    var safe = 0

    file.forEachLine { line -> 
        val nums = line.split("\\s+".toRegex()).map { it.toInt() }

        if (isSafe(nums)) {
            safe += 1
            return@forEachLine
        }
        
        var safeLines = 0
        for (i in nums.indices) {
            val copy = ArrayList(nums)
            copy.removeAt(i)
            safeLines += if (isSafe(copy)) 1 else 0
        }

        safe += if (safeLines >= 1) 1 else 0
    }

    return safe
}

fun main() {
    println(day2part1("day2.input"))
    println(day2part2("day2.input"))
}
