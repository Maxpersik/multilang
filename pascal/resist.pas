Uses SysUtils, Math;

var R, S : float; i : integer;

begin 
    S := 0;
    for i := 1 to ParamCount do
    begin
        S := S + 1/StrToFloat(ParamStr(i));
    end;
    R := 1/S;
    Writeln('Общее сопротивление равно: ', R:0:2,' Ом');
end.

