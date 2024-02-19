var express = require('express');
var router = express.Router();
var accountController = require('../controllers/accountController');
const { authenticateTokenFromHeaders } = require('../jwtFunctions');


router.get('/', authenticateTokenFromHeaders, accountController.getProfileUser);

router.post('/user', authenticateTokenFromHeaders, accountController.createProfile);

router.post('/signup', accountController.signup);

router.post('/login', accountController.login);

router.put('/user', authenticateTokenFromHeaders, accountController.updateProfile);

router.put('/updatePassword', authenticateTokenFromHeaders, accountController.updatePassword)


module.exports = router;