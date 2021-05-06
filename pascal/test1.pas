var n, s: integer;
begin
    n := 1;
    s := 0;
    while n <= 100 do
    begin
        s := s + 30;
        n := n * 2;
    end;
    write(s);
end.
