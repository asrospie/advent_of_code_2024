def parse_rules_and_updates(filename)
  page_rules = {}
  page_numbers = []

  reading_rules = true
  File.open(filename, 'r') do |f|
    while line = f.gets
      line = line.strip

      if line == "" and reading_rules
        reading_rules = false
        next 
      end

      if line == "" and not reading_lines
        break
      end

      if reading_rules
        line = line.split "|"
        if !page_rules.key? line[0] 
          page_rules[line[0]] = []
        end

        page_rules[line[0]] << line[1]
      else
        page_numbers << line.split(",")
      end
    end
  end

  return page_rules, page_numbers
end


def find_bad_updates(page_rules, page_updates)
  bad_updates = []

  page_updates.each do |pg|
    failed = false

    ((pg.length - 1)..0).each do |i|
      v = pg[i]

      if not page_rules.key? v
        next
      end

      ((i - 1)..0).each do |j|
        if page_rules.fetch(v).includes?(pg[j])
          failed = true
          bad_updates << pg
        end
      end
      if failed
        break
      end
    end
  end

  return bad_updates
end


def main()
  puts parse_rules_and_updates 'day_5.test'
end


if __FILE__ == $0
  main()
end
