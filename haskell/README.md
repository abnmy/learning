```haskell
-- single line comment
{- multi line comment
`cd` to the working directory please!
docker run -v `pwd`:`pwd` -w `pwd` -it --rm haskell:8
https://docs.docker.com/engine/reference/commandline/run/#mount-volume--v---read-only
-}

-- :l <filename> (load file)
-- :r (reload)

doubleMe x = x + x

-- doubleUs x y = x*2 + y*2
doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100
    then x
    else x*2

doubleSmallNumber' x = (if x > 100 then x else x*2)+1

-- let xx = 123 (only in ghci)
xx = 123
```
