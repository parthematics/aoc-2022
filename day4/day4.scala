import scala.io.Source

object Main {
    def fullyContainsOther(firstAssignment: List[Int], secondAssignment: List[Int]): Boolean = {
        val firstInSecond: Boolean = (firstAssignment(0) >= secondAssignment(0)) && (firstAssignment(1) <= secondAssignment(1))
        val secondInFirst: Boolean = (secondAssignment(0) >= firstAssignment(0)) && (secondAssignment(1) <= firstAssignment(1))
        firstInSecond || secondInFirst
    }

    def overlaps(firstAssignment: List[Int], secondAssignment: List[Int]): Boolean = {
        (firstAssignment, secondAssignment) match {
            case (_, _) if firstAssignment(0) <= secondAssignment(0) => secondAssignment(0) <= firstAssignment(1)
            case _ => firstAssignment(0) <= secondAssignment(1)
        }
    }

    // Part 1
    def fullyContainedAssignmentPairs(filename: String): Int = {
        Source.fromFile(filename).getLines().toList.map { str =>
            val assignments: List[List[Int]] = str.split(",").toList.map { assignmentStr =>
                assignmentStr.split("-").toList.map(_.toInt) 
            }
            if (fullyContainsOther(assignments.head, assignments.last)) 1 else 0
        }.reduceLeft(_ + _)
    }

    // Part 2
    def overlappingAssignmentPairs(filename: String): Int = {
        Source.fromFile(filename).getLines().toList.map { str =>
            val assignments: List[List[Int]] = str.split(",").toList.map { assignmentStr =>
                assignmentStr.split("-").toList.map(_.toInt) 
            }
            if (overlaps(assignments.head, assignments.last)) 1 else 0
        }.reduceLeft(_ + _)
    }

    def main(args: Array[String]): Unit = {
        val testInputFile = "day4_test.txt"
        val mainInputFile = "day4.txt"
        // Part 1
        println(fullyContainedAssignmentPairs(mainInputFile))
        // Part 2
        println(overlappingAssignmentPairs(mainInputFile))
    }
}