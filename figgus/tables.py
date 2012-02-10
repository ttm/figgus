class Tables:
    f=open("figgus/tables/sin1024.txt","r")
    sin1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("figgus/tables/sin2048.txt","r")
    sin2048=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("figgus/tables/saw1024.txt","r")
    saw1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("figgus/tables/saw2048.txt","r")
    saw2048=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("figgus/tables/wnoise1024.txt","r")
    wnoise1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("figgus/tables/wnoise2048.txt","r")
    wnoise2048=[float(i) for i in f.read().split(",")]
    f.close()