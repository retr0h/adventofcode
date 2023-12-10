package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

var cubeLimitMap = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func getCountsForRegexp(re *regexp.Regexp, line string) []int {
	counts := []int{}
	matches := re.FindAllStringSubmatch(line, -1)
	for _, v := range matches {
		count, err := strconv.Atoi(string(v[1]))
		if err != nil {
			count = 0
		}
		counts = append(counts, count)
	}

	return counts
}

func getPossibleGames(file *os.File) (map[int]map[string][]int, error) {
	scanner := bufio.NewScanner(file)
	gameMap := make(map[int]map[string][]int)
	for scanner.Scan() {
		// should just  regexp
		// Game 74: 6 blue, 4 red, 4 green; 17 green, 1 blue; 4 blue, 7 green, 4 red
		gameSlice := strings.Split(scanner.Text(), ":")
		head := gameSlice[0]
		tail := gameSlice[1]

		gameNumberString := strings.Split(head, " ")[1]
		gameNumber, err := strconv.Atoi(gameNumberString)
		if err != nil {
			return nil, err
		}

		redCounts := getCountsForRegexp(regexp.MustCompile(`(\d+) red`), tail)
		greenCounts := getCountsForRegexp(regexp.MustCompile(`(\d+) green`), tail)
		blueCounts := getCountsForRegexp(regexp.MustCompile(`(\d+) blue`), tail)

		gameMap[gameNumber] = map[string][]int{
			"red":   redCounts,
			"green": greenCounts,
			"blue":  blueCounts,
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return gameMap, nil
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	possibleGames, err := getPossibleGames(file)
	if err != nil {
		log.Fatal(err)
	}

	// Determine which games would have been possible if the bag had been loaded
	// with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
	// of the IDs of those games?
	sum := 0
	for _, game := range possibleGames {
		redMax := slices.Max(game["red"])
		greenMax := slices.Max(game["green"])
		blueMax := slices.Max(game["blue"])

		power := redMax * greenMax * blueMax
		sum += power
	}

	fmt.Println(sum)

	if sum != 63711 {
		panic("broke it")
	}
}
