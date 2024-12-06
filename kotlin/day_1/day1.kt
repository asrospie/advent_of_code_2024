import java.io.File
import kotlin.math.abs

fun day1part1(): Int {
    val filename = "day1.input"
    val file = File(filename)

    val left = arrayListOf<Int>()
    val right = arrayListOf<Int>()

    if (file.exists()) {
        file.forEachLine { line -> 
            val words = line.split("\\s+".toRegex())
            left.add(words[0].toInt())
            right.add(words[1].toInt())
        }
    } else {
        println("File not found: $filename")
    }

    left.sort()
    right.sort()

    var result = 0
    for (i in left.indices) {
        result += abs(left[i] - right[i])
    }


    return result
}

fun day1part2(): Int {
    val filename = "day1.input"
    val file = File(filename)

    val left = arrayListOf<Int>()
    val right = mutableMapOf<Int, Int>()

    if (file.exists()) {
        file.forEachLine { line ->
            val words = line.split("\\s+".toRegex())

            left.add(words[0].toInt())

            val rightVal = words[1].toInt()
            right[rightVal] = right.getOrPut(rightVal) { 0 }.inc()
        }
    } else {
        println("File not found: $filename")
    }

    var result = 0
    for (l in left) {
        if (right.containsKey(l)) {
            result += l * right.getValue(l)
        }
    }

    return result
}

fun main() {
    println(day1part1())
    println(day1part2())
}
