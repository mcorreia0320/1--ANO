const jwt = require('jsonwebtoken'); 

function authenticateTokenFromHeaders(req, res, next) {
    // Gather the jwt access token from the request header
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; 
    // Unauthorized
    if (token == null) return res.sendStatus(401);
      jwt.verify(token, process.env.TOKEN_SECRET, (err, user) => {
      if (err)
        return res.sendStatus(403); // Forbidden
      req.user = user;
      next();
    });
  }

  function generateAccessToken(email, password) {
    var token = jwt.sign({ email, password }, process.env.TOKEN_SECRET, { expiresIn: '1800s' });
    return token;
}

module.exports = { authenticateTokenFromHeaders, generateAccessToken};