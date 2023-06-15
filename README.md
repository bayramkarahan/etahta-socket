# mesaj-Örneği
Bu proje nodejs ile yapılmış socketio yapısı kullanılmıştır.
socketio ile server-client uygulaması oluşturulmuştur. 
Oluşturulan proje heroku.com üzerinden oluşturulan hesapla yayınlanmış ve istemci erişimine açılmıştır.

# Socketio Nedir?
Socket.io, gerçek zamanlı, çift yönlü ve olay tabanlı iletişim sağlamak için kullanılan bir JavaScript kütüphanesidir. Bu kütüphane, sunucu ve istemci arasında veri akışını sağlamak için WebSocket protokolünü kullanır. WebSocket protokolü, sunucu ve istemci arasında tam çift yönlü iletişim sağlar ve bu sayede gerçek zamanlı uygulamalar geliştirmek mümkün hale gelir.

Socket.io, WebSocket protokolünün yanı sıra, HTTP uzun süreli bağlantıları (long-polling), AJAX polling ve diğer teknolojileri de destekler. Bu sayede, Socket.io, farklı tarayıcılar ve cihazlar arasında uyumlu bir şekilde çalışabilir.

Socket.io, olay tabanlı bir yapıya sahiptir. Bu sayede, sunucu ve istemci arasında farklı olaylar tetiklenebilir ve bu olaylar üzerinden veri akışı sağlanabilir. Örneğin, bir kullanıcının mesaj göndermesi gibi bir olay tetiklendiğinde, bu olay sunucu tarafından alınır ve diğer kullanıcılara gönderilir. Bu sayede, gerçek zamanlı sohbet uygulamaları gibi uygulamalar geliştirmek mümkün hale gelir.

Socket.io, Node.js ile birlikte kullanılabildiği gibi, farklı programlama dilleri ve platformlarla da uyumlu bir şekilde çalışabilir. Bu sayede, farklı uygulama senaryolarına uygun bir şekilde kullanılabilir.

Özetle, Socket.io, gerçek zamanlı, çift yönlü ve olay tabanlı iletişim sağlamak için kullanılan bir JavaScript kütüphanesidir. WebSocket protokolü ve diğer teknolojilerle uyumlu bir şekilde çalışabilmesi sayesinde, farklı uygulama senaryolarına uygun bir şekilde kullanılabilir.

# heroku.com nedir?
Heroku, bulut tabanlı bir platform hizmetidir. Geliştiricilerin uygulamalarını, veritabanlarını ve diğer hizmetleri barındırmalarına olanak tanır. Heroku, uygulamaların hızlı bir şekilde dağıtılmasını, ölçeklendirilmesini ve yönetilmesini sağlar.

Heroku, geliştiricilerin uygulamalarını barındırmak için birçok programlama dilini destekler. Bunlar arasında Node.js, Ruby, Python, Java, PHP ve daha birçok dildir. Heroku, geliştiricilerin uygulamalarını barındırmak için birçok farklı veritabanı hizmeti sunar. Bunlar arasında PostgreSQL, MySQL, MongoDB ve Redis gibi popüler veritabanları yer alır.

Heroku, geliştiricilerin uygulamalarını hızlı bir şekilde dağıtmalarına olanak tanır. Geliştiriciler, uygulamalarını GitHub, Bitbucket veya GitLab gibi bir Git deposundan Heroku'ya bağlayabilirler. Heroku, uygulamayı otomatik olarak derleyip dağıtır. Bu, geliştiricilerin uygulamalarını hızlı bir şekilde yayınlamalarına olanak tanır.

Heroku, uygulamaların ölçeklendirilmesini kolaylaştırır. Geliştiriciler, uygulamalarını tek bir işlemci çekirdeğinden binlerce işlemci çekirdeğine kadar ölçeklendirebilirler. Bu, uygulamanın trafik yüküne göre otomatik olarak ölçeklendirilmesini sağlar.

Heroku, geliştiricilerin uygulamalarını yönetmelerine olanak tanır. Heroku, uygulamaların performansını, kaynak kullanımını ve diğer istatistikleri izlemek için birçok araç sunar. Ayrıca, uygulamaların güvenliğini sağlamak için birçok güvenlik özelliği sunar.

Sonuç olarak, Heroku, geliştiricilerin uygulamalarını hızlı bir şekilde dağıtmalarına, ölçeklendirmelerine ve yönetmelerine olanak tanır. Heroku, birçok programlama dili ve veritabanı hizmeti desteği sunar. Bu nedenle, Heroku, geliştiricilerin uygulamalarını barındırmak için popüler bir seçenektir.


# Sunucu Kodumuz
````
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  socket.on('chat message', msg => {
    io.emit('chat message', "bayram"+ msg);
  });
});

http.listen(port, () => {
  console.log(`Socket.IO server running at http://localhost:${port}/`);
});
````

# Istemci Kodumuz
````
const
    io = require("socket.io-client"),
    ioClient = io.connect("http://localhost:3000");

ioClient.on("seq-num", (msg) => console.info(msg));
````

# github ile heroku bağlamak
Github ve Heroku arasındaki bağlantıyı kurmak oldukça kolaydır. İlk olarak, Github hesabınızda bir depo oluşturmanız gerekir. Bu depo, Heroku'ya yükleyeceğiniz uygulamanın kaynak kodlarını içerecektir. Ardından, Heroku hesabınızda bir uygulama oluşturmanız gerekir. Bu uygulama, Github'daki depodan alınan kaynak kodlarını barındıracaktır.

Github ve Heroku arasındaki bağlantıyı kurmak için aşağıdaki adımları izleyebilirsiniz:
````
Github hesabınızda bir depo oluşturun.
Heroku hesabınızda bir uygulama oluşturun.
Heroku Dashboard'da, "Deploy" sekmesine gidin ve "Deployment Method" bölümünde "Github" seçeneğini seçin.
Github hesabınızla Heroku hesabınızı bağlamak için "Connect to Github" düğmesine tıklayın.
Github hesabınızda, Heroku'ya yükleyeceğiniz uygulamanın kaynak kodlarını içeren depoyu seçin.
Heroku Dashboard'da, "Manual Deploy" bölümünde "Deploy Branch" düğmesine tıklayın.
Bu adımları takip ettikten sonra, Github ve Heroku arasındaki bağlantı kurulmuş olacaktır. Artık, Github'daki depodaki değişiklikler Heroku'ya otomatik olarak yüklenecektir.
````

This is the source code for a very simple chat example used for
the [Getting Started](http://socket.io/get-started/chat/) guide
of the Socket.IO website.

Please refer to it to learn how to run this application.

You can also spin up a free Heroku dyno to test it out:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/socketio/chat-example)

Or run it on [Repl.it](https://repl.it/):

[![Run on Repl.it](https://repl.it/badge/github/socketio/chat-example)](https://repl.it/github/socketio/chat-example)
# etahta-socket
