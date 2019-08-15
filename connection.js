const mongoose = require('mongoose');

// connect to MONGO_DBNAME
mongoose.connect('mongodb://localhost/food_app');

mongoose.connection.once('open',function(){
  console.log('Connection has been made, now');
}).on('error',function(error){
  console.log('Connection error:', error);
});
