----defines a factorial function
--function fact(n)
--    if n==0 then
--        return 1
--    else
--        return n*fact(n-1)
--    end
--end
--
--print("enter a number:")
--a=io.read("*numbexcr")  --read a number
--print(fact(a))
--****************************************
--function foo(a,b,c)
--    local sum=a+b
--    return sum, c
--end
--r1,r2=foo(1,'123','hello')
--print(r1,r2)
--****************************************
--a={}
--b={n=1,str='abc',100,'hello'}
--a.n=1
--a.str='abc'
--a[1]=100
--a[2]='hello'
--a["a table"]=b
--for k,v in pairs(a) do
--    print(k,"=>",v)
--end
--****************************************
--function createFoo(name)
--    local obj={name=name}
--    function obj:SetName(name)
--        self.name=name
--    end
--    function obj:GetName()
--        return self.name
--    end
--    return obj
--end
--o=createFoo("Sam")
--print("name:",o:GetName())
--
--o:SetName("Lucy")
--print("name:",o:GetName())
--***************************************
--function createCountdownTimer(second)
--    local ms = second*1000
--    local function countDown()
--        ms=ms-1
--        return ms
--    end
--    return countDown
--end
--timer1=createCountdownTimer(1)
--for i=1,3 do
--    print(timer1())
--end
--print("------------------")
--timer2=createCountdownTimer(1)
--for i=1,3 do
--    print(timer2())
--end
--*****************************************
--function createFoo(name)
--    local data={name=name}
--    local obj={}
--    function obj.SetName(name)
--        data.name=name
--    end
--    function obj.GetName()
--        return data.name
--    end
--    return obj
--end
--o=createFoo("Sam")
--print("name:",o.GetName())
--o.SetName("Lucy")
--print("name:",o.GetName())
--******************************************
--t={}
--t2={a=" and ",b="LiLei",c="Han Meimei"}
--m={__index=t2}
--setmetatable(t,m)
--for k,v in pairs(t) do
--    print(k,v)
--end
--print("------------")
--print(t.b, t.a,t.c)
--******************************************
function add(t1,t2)
    local length=#t1
    for i = 1,length do
        t1[i]=t1[i]+t2[i]
    end
    return t1
end
t1={1,2,3}
t2={10,20,30}
setmetatable(t1,{__add=add})
setmetatable(t2,{__add=add})
t1=t1+t2
for i=1,#t1 do
    print(t1[i])
end

