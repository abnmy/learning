```ruby
#!/usr/bin/env ruby

# https://www.ruby-lang.org/en/documentation/quickstart/
# docker run -it --rm ruby:2.7.2
# docker run -v `pwd`:`pwd` -w `pwd` -it --rm ruby:2.7.2

# load "new.rb"
# require "./new.rb"

"hello"
puts "hello"

3+2
Math.sqrt(9)

a = 1+7

def hi
    puts "hee"
end
hi
hi()

def hello(name="world")
    puts "hello #{name.capitalize}!"
end
hello("francis")
hello "vanessa"
hello

class G
    def initialize(name="bob")
        @name = name
    end
    def hi
        puts "hi #{@name}"
    end
end
G.instance_methods  # all
G.instance_methods(false)  # only local methods

greeter = G.new("vanessa")
greeter.respond_to?("hi")  # true
greeter.hi

greeter.respond_to?("to_s")  # true

greeter.respond_to?("name")  # false

class G
    attr_accessor :name  # The changes will be available in existing objects of that class!!
end
greeter.respond_to?("name")  # true
greeter.respond_to?("name=")  # true
greeter.name="Sophie"



class MegaGreeter
    attr_accessor :names

    # Create the object
    def initialize(names = "World")
        @names = names
    end

    # Say hi to everybody
    def say_hi
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("each")
            # @names is a list of some kind, iterate!
            @names.each do |name|
                puts "Hello #{name}!"
            end
        else
            puts "Hello #{@names}!"
        end
    end

    # Say bye to everybody
    def say_bye
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("join")  # relying on what methods it supports is known as “Duck Typing”
            # Join the list elements with commas
            puts "Goodbye #{@names.join(", ")}.  Come back soon!"
        else
            puts "Goodbye #{@names}.  Come back soon!"
        end
    end
end


if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
    mg.say_bye

    # Change name to be "Zeke"
    mg.names = "Zeke"
    mg.say_hi
    mg.say_bye

    # Change the name to an array of names
    mg.names = ["Va", "ne", "ssa"]
    mg.say_hi
    mg.say_bye

    # Change to nil
    mg.names = nil
    mg.say_hi
    mg.say_bye
end
```
