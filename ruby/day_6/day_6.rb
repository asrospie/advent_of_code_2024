def display_grid(grid)
  grid.each do |line|
    puts line.join("")
  end
end


def parse_grid(filename)
  grid = []

  File.open(filename, 'r') do |f|
    f.each_line { |line| 
      grid << line.strip.split("")
    }
  end

  starting_coord = [0, 0]
  grid.each_with_index do |line, y|
    x = line.index "^"
    if x != nil
      starting_coord = [x, y]
    end
  end

  [starting_coord, grid]
end


def day_6_part_1(filename)
  start, grid = parse_grid filename
  grid[start[1]][start[0]] = "X"

  # current direction U, D, L, R
  cur_dir = :up
  # mark starting location as visited
  visited = [[[start[0], start[1]], :up]]

  steps = 1
  cursor = [start[0], start[1]]
  loop do
    case cur_dir
    when :up
      if cursor[1] - 1 < 0
        break
      end
      if grid[cursor[1] - 1][cursor[0]] == "#"
        cur_dir = :right
        next
      end
      cursor[1] -= 1
    when :down
      if cursor[1] + 1 >= grid.length
        break
      end
      if grid[cursor[1] + 1][cursor[0]] == "#"
        cur_dir = :left
        next
      end
      cursor[1] += 1
    when :left
      if cursor[0] - 1 < 0
        break
      end
      if grid[cursor[1]][cursor[0] - 1] == "#"
        cur_dir = :up
        next
      end
      cursor[0] -= 1
    when :right
      if cursor[0] + 1 >= grid[0].length
        break
      end
      if grid[cursor[1]][cursor[0] + 1] == "#"
        cur_dir = :down
        next
      end
      cursor[0] += 1
    end

    if visited.include? [cursor, cur_dir]
      break
    end

    visited << [[cursor[0], cursor[1]], cur_dir]
    if grid[cursor[1]][cursor[0]] != "X"
      grid[cursor[1]][cursor[0]] = "X"
      steps += 1
    end

  end

  [steps, start, visited]
end


def is_ninety_degrees?(dir_one, dir_two)
  case [dir_one, dir_two]
  when [:up, :right]
    true
  when [:right, :down]
    true
  when [:down, :left]
    true
  when [:left, :up]
    true
  else
    false
  end
end


def is_loop?(grid, start)
  # current direction U, D, L, R
  cur_dir = :up
  # mark starting location as visited
  visited = [[[start[0], start[1]], :up]]

  cursor = [start[0], start[1]]
  loop do
    case cur_dir
    when :up
      if cursor[1] - 1 < 0
        return false
      end
      if grid[cursor[1] - 1][cursor[0]] == "#"
        cur_dir = :right
        next
      end
      cursor[1] -= 1
    when :down
      if cursor[1] + 1 >= grid.length
        return false
      end
      if grid[cursor[1] + 1][cursor[0]] == "#"
        cur_dir = :left
        next
      end
      cursor[1] += 1
    when :left
      if cursor[0] - 1 < 0
        return false
      end
      if grid[cursor[1]][cursor[0] - 1] == "#"
        cur_dir = :up
        next
      end
      cursor[0] -= 1
    when :right
      if cursor[0] + 1 >= grid[0].length
        return false
      end
      if grid[cursor[1]][cursor[0] + 1] == "#"
        cur_dir = :down
        next
      end
      cursor[0] += 1
    end

    if visited.include? [cursor, cur_dir]
      return true 
    end

    visited << [[cursor[0], cursor[1]], cur_dir]

  end

end


def day_6_part_2(filename)
  start, grid = parse_grid filename

  count = 0
  (0...grid.length).each do |y|
    (0...grid[0].length).each do |x|
      next if grid[y][x] != "."

      grid[y][x] = "#"
      if is_loop?(grid, start) then count += 1 end
      grid[y][x] = "."
    end
  end

  count
end


def main
  # puts day_6_part_1("day_6.test")[0]
  # puts day_6_part_1("day_6.input")[0]
  puts day_6_part_2 "day_6.test"
  puts day_6_part_2 "day_6.input"
end


if __FILE__ == $0
  main
end
