import scala.io.Source

object day_1 extends App {

    val file: String = "../input/input_1.txt"
    var elves = Set()
    var calories: Int = 0
    var elf: Int = 1

    for (line <- Source.fromFile(file).getLines.mkString) {

        if (line != "\n\n") {
            println(line)
        }

    }

}