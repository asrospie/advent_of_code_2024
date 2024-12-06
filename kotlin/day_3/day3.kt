import java.io.File
import kotlin.text.Regex

fun day3part1(filename: String): Int {
    val file = File(filename)

    if (!file.exists()) {
        println("$filename does not exist")
        return -1
    }
    
    val fileContents = file.readText();
    val regex = Regex("mul\\((\\d+,\\d+)\\)")

    val matchResult = regex.findAll(fileContents)

    var result = 0
    for (match in matchResult) {
        val nums = match.groupValues[1].split(",").map { it.toInt() }
        result += nums[0] * nums[1] 
    }

    return result
}

fun day3part2(filename: String): Int {
    val file = File(filename)

    if (!file.exists()) {
        println("$filename does not exist")
        return -1
    }

    val fileContents = file.readText()
    val regex = Regex("mul\\((\\d+,\\d+)\\)|do\\(\\)|don't\\(\\)")

    val matchResults = regex.findAll(fileContents)

    var result = 0
    var ignore = false
    for (match in matchResults) {
        if (match.value == "don't()") {
            ignore = true
            continue
        }
        if (match.value == "do()") {
            ignore = false
            continue
        }

        if (!ignore) {
            val nums = match.groupValues[1].split(",").map { it.toInt() }
            result += nums[0] * nums[1]
        }
    }

    return result
}

fun main() {
    println(day3part1("test3.txt"))
    println(day3part1("day3.input"))
    println(day3part2("test32.txt"))
    println(day3part2("day3.input"))
}
