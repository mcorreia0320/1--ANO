var express = require('express');
var router = express.Router();
var indexController = require('../controllers/indexControllers')

/* GET home page. */
router.get('/', indexController.getAllUser);

module.exports = router;
