var express = require('express');
var router = express.Router();
var indexController = require('../controllers/indexControllers');

router.get('/grades', indexController.getAllGrades);
router.post('/grades', indexController.createGrade);
router.delete('/grades', indexController.deleteGrade);
router.patch('/grades/:student_id/:course_id', indexController.updateGrade);
router.get('/grades/:student_id', indexController.getAllGradesForOneStudent);
router.get('/log');

module.exports = router;
