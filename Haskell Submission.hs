ack :: Int -> Int -> Int
ack 0 n = n+1
ack m 0 = ack (m-1) 1
ack m n = ack (m-1) (ack m (n-1))

number = ack 99999 99999
dosomething 0 = return ()
dosomething n =
    do
        putStrLn "OMG Haskell"
        nothing <- getLine
        dosomething (n-1)

main = dosomething number
