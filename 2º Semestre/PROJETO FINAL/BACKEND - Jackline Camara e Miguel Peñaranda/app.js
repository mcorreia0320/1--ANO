var dotenv = require('dotenv');
dotenv.config();

var express = require('express');
var session = require('express-session');
var cookieParser = require('cookie-parser');
var path = require('path');
var flash = require('connect-flash');
var cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger-output.json');

var accountRouter = require('./routes/account');
var landingPageRouter = require('./routes/landingPage');
var calculatorRouter = require('./routes/calculator');
var administradorRouter = require('./routes/administrador');

var app = express();

app.use(cors());

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(cookieParser()); // read cookies (needed for auth)
app.use(express.json()); // get information from html forms
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));



// Use the session middleware
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true   
}));

app.use(flash()); // use connect-flash for flash messages stored in session

app.use('/api-docs',swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.use('/account', accountRouter);
app.use('/landingpage', landingPageRouter);
app.use('/calculator', calculatorRouter);
app.use('/admin', administradorRouter);


module.exports = app;