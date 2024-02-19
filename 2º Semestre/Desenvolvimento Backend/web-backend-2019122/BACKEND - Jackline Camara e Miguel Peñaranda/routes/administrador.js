var express = require('express');
var router = express.Router();
var administradorController = require('../controllers//administradorController');
const { authenticateTokenFromHeaders } = require('../jwtFunctions');

router.use(authenticateTokenFromHeaders);

router.get('/', administradorController.getInfoUsers);
router.delete('/', administradorController.DeleteAccount);


module.exports = router;