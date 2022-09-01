function root = Newton(x0, E, imax, f, fp)
i = 1
fprintf( ' iteration   approximation \n')

for i = 1:n
    root = x0 - (f(x0))/(fp(x0)
    fprintf( ' %6.0f %18.8f \n' , i, root )
    
    if 1-x0/root < E
    end
i = i+1
x0 = root

else
    fprintf( ' failed to converge in %g iterations\n', imax)
      
end

