from PIL import Image, ImageDraw, ImageFont

W,H=900,520
BG=(13,17,23); PANEL=(22,27,34); TEXT=(230,237,243); MUTED=(139,148,158)
GREEN=(46,160,67); BLUE=(88,166,255); ACCENT=(255,200,80); PURPLE=(188,140,255)

def font(size,bold=False,mono=False):
    base="/usr/share/fonts/truetype/dejavu/"
    if mono:
        name="DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
    else:
        name="DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(base+name,size)

server=[
"$ cd springcloudServer",
"$ ./mvnw spring-boot:run",
"",
"Tomcat started on port(s): 8800",
"Started SpringcloudApplication",
"",
"$ curl localhost:8800/application/default",
'{"name":"application", ...}',
]
client=[
"$ cd springcloudClient",
"$ ./mvnw spring-boot:run",
"",
"Fetching config from : http://localhost:8800",
"Located environment: application/default",
"Tomcat started on port(s): 8801",
"",
"$ curl localhost:8801/config/max-attempts",
"5",
]
frames=[]

for i in range(62):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.text((34,20),"Spring Cloud Network",font=font(28,True),fill=TEXT)
    d.text((34,56),"Config Server → Config Client → REST endpoint",font=font(16),fill=MUTED)
    d.rounded_rectangle((35,93,865,145),radius=14,fill=(25,32,40))
    d.text((54,105),"config-repo/application.properties",font=font(14,True,True),fill=BLUE)
    value="spring.maxAttempts=5"
    d.text((380,105),value[:max(0,min(len(value),i-2))],font=font(16,False,True),fill=ACCENT)

    left=(35,165,430,470); right=(470,165,865,470)
    for box,title,accent in [(left,"CONFIG SERVER :8800",GREEN),(right,"CONFIG CLIENT :8801",PURPLE)]:
        d.rounded_rectangle(box,radius=16,fill=PANEL)
        d.rectangle((box[0],box[1],box[2],box[1]+38),fill=(30,36,44))
        d.text((box[0]+18,box[1]+10),title,font=font(14,True,True),fill=accent)
        for j,col in enumerate([(248,81,73),(255,200,80),(46,160,67)]):
            d.ellipse((box[2]-68+j*18,box[1]+14,box[2]-58+j*18,box[1]+24),fill=col)

    server_count=0 if i<14 else min(len(server),1+(i-14)//3)
    client_count=0 if i<34 else min(len(client),1+(i-34)//3)
    y=215
    for line in server[:server_count]:
        col=GREEN if ("Started" in line or "Tomcat started" in line) else (BLUE if line.startswith("$") else TEXT)
        if "{" in line: col=ACCENT
        d.text((53,y),line,font=font(12,False,True),fill=col); y+=26 if line else 15
    y=215
    for line in client[:client_count]:
        col=GREEN if line=="5" else (PURPLE if ("Fetching config" in line or "Located" in line) else (BLUE if line.startswith("$") else TEXT))
        d.text((488,y),line,font=font(22,True,True) if line=="5" else font(12,False,True),fill=col)
        y+=28 if line else 15

    d.line((430,315,470,315),fill=MUTED,width=2)
    d.polygon([(463,309),(470,315),(463,321)],fill=MUTED)
    if i>=34: d.text((435,290),"config",font=font(11,True),fill=ACCENT)
    if i>=57:
        d.rounded_rectangle((285,477,615,509),radius=12,fill=(26,48,35))
        d.text((316,483),"✓ end-to-end HTTP smoke test passed",font=font(13,True),fill=GREEN)
    frames.append(im)

frames[0].save("demo.gif",save_all=True,append_images=frames[1:],duration=115,loop=0,optimize=True,disposal=2)
