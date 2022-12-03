import scala.io.Source

object Main {
    def getPriority(letter: Char): Int = {
        if (letter.isLower) {
            letter.toInt - 'a'.toInt + 1
        } else {
            letter.toInt - 'A'.toInt + 27
        }
    }

    // Part 1
    def prioritySum(filename: String): Int = {
        val rucksacks: List[String] = Source.fromFile(filename).getLines.toList
        val priorities: List[Int] = rucksacks.map { str =>
            val firstCompartment: Set[Char] = str.slice(0, str.length / 2).toSet
            val secondCompartment: Set[Char] = str.slice(str.length / 2, str.length).toSet
            val repeatedItem: Char = firstCompartment.intersect(secondCompartment).head
            repeatedItem
        }.map { getPriority(_) }
        val sum: Int = priorities.foldLeft(0)(_ + _)
        sum
    }

    // Part 2
    def prioritySumBadges(filename: String): Int = {
        val groupRucksacks: List[List[String]] = Source.fromFile(filename).getLines.toList.grouped(3).toList
        val badgePriorities: List[Int] = groupRucksacks map { 
            group => group.map(_.toSet).reduceLeft(_ intersect _).head 
        } map { getPriority(_) }
        val sum: Int = badgePriorities.foldLeft(0)(_ + _)
        sum
    }

    def main(args: Array[String]): Unit = {
        val testInputFile = "day3_test.txt"
        val mainInputFile = "day3.txt"
        // Part 1
        println(prioritySum(mainInputFile))
        // Part 2
        println(prioritySumBadges(mainInputFile))
    }
}