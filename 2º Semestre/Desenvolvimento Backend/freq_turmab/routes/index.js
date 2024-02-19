var express = require('express');
var indexController = require('../controllers/indexController');
var router = express.Router();


router.get('/appointments', indexController.getAllApoitnments);
router.post('/appointments', indexController.CreateAppointment);
router.delete('/appointments/:appointment_id', indexController.deleteAppointment);
router.patch('/appointments/:patient_id/:dentist_id', indexController.updateAppointment);
router.get('/appointments/patient/', indexController.getAppointmentsOfPatient);
router.get('/log', indexController.downloadLog);

module.exports = router;
