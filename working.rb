require 'open-uri'
require 'nokogiri'
site = "https://codereview.stackexchange.com/"
system 'cls'
system("color 0a")
10.times do
    begin
        id = rand(1..6000)
        url = "#{site}/a/#{id}"
        tries = 3
        begin
            page = Nokogiri::HTML(open(url))
        rescue OpenURI::HTTPRedirect => redirect
            page = Nokogiri::HTML(open(url))
            retry if (tries -= 1) > 0
            raise
        end
        code = page.css('code')[0].text
    end until code

    code.each_char  do |char|
        print char
        sleep rand(10) / 30.0
    end
end
