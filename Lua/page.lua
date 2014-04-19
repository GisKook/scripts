--page=[[
--<html>
--<head>
--<title>An HTML Page</title>
--</head>
--<body>
-- <a href="http://www.lua.org">Lua</a>
--</body>
--</html>
--]]
--
--io.write(page)
line=io.read()
n = tonumber(line)
if n==nil then
    error(line .. "is not a valid number")
else
    print(n*2)
end
