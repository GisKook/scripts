--***********************if/elseif/else/end
print("please input left number")
local l=io.read("*number")
if l==nil then
    print("I need a number!")
    os.exit(0)
end

local r
print("please input right number")
r=io.read("*number")
if r==nil then
    print("I need a number!")
    os.exit(0)
end

local rr
print("please choice operater '+' '-' '*' '/'")
local op=io.read()
op="4"
print(tonumber(op))
if op=="+" then
    rr=l+r
elseif op=="-" then
    rr=l-r
elseif op=="*" then
    rr=l*r
elseif op=="/" then
    rr=l/r
else
    error("invalid operation")
end
print(rr)
----***********************repeat/until
--repeat 
--    line=io.read()
--    print(line)
--until line=="gis"
