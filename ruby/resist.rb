#!/usr/bin/ruby

s = 0
for r in ARGV do
    s += 1/r.to_f
end
rs = 1/s
puts "Общее сопротивление равно: " + rs.round(2).to_s + " Ом"
