const { Appointment, Patient, Dentist } = require('../sequelize');

exports.getAllApoitnments = (req, res, next) =>{
    Appointment.findAll({include: [Patient, Dentist]}).then(result =>{
        if ( result == null) {
            res.status(404).send('Não foi encontrada nenhuma marcação!')
        } else res.status(200).send(result);
    })
}
exports.CreateAppointment = (req, res, next) =>{
    const { date, duration, dentist, patient  } = req.body;

    if (date === "" || duration === "" || dentist === "" || patient === "" ) {
        res.status(400).send("Por favor preencha todos os campos!")
    } 
    else {
        Dentist.findByPk(dentist).then( dentist_result =>{
            if (dentist_result == null) {
                res.status(404).send('O dentista selecionado não existe!')
            } 
            else {
                Patient.findByPk(patient).then(patient_result =>{
                    if (patient_result == null) {
                        res.status(404).send('O paciente selecionado não existe!')
                    } 
                    else{
                        Appointment.create({appointment_datetime: date, duration_minutes: duration, patient_id: patient, dentist_id: dentist }).then( appointment =>{
                            if (appointment == null) {
                                res.status(500).send("Ocorreu um problema!");
                            } else res.status(200).send("Foi marcada a sua consulta com o ID: " + appointment.appointment_id + " e o horario é: " + appointment.appointment_datetime);
                        })
                    }
                })
            }
        })
    }
}

exports.deleteAppointment = (req, res, next) =>{
    const id = req.params.appointment_id;

    Appointment.findByPk(id).then(result =>{
        if ( result == null ) {
            res.status(404).send("A marcação com o ID: " + id + " não existe!")
        } else {
            Appointment.destroy({where: {appointment_id: id}}).then(rowCount =>{
                res.status(200).send("A marcação com o ID: " + id + " foi eliminada com successo e o número de linhas afetadas foi: " + rowCount);
            })
        }
    })
}

exports.updateAppointment = (req, res, next)=>{
    const { patient_id, dentist_id} = req.params;
    const { date } = req.body;

    
    Patient.findByPk(patient_id).then(result =>{
        if ( result == null ) {
            res.status(404).send("Não existe o paciente indicado!")
        } else {
            Dentist.findByPk(dentist_id).then(result =>{
                if ( result == null ) {
                    res.status(404).send("Não existe o dentista indicado!")
                } else {
                    Appointment.findOne({where:{'patient_id': patient_id, 'dentist_id': dentist_id}}).then(result=>{
                        if (result == null) {
                            res.status(400).send("Não existe nenhuma marcação entre o paciente com o ID: " + patient_id + " e o dentista com o ID: " + dentist_id);
                        } else {
                            Appointment.update({appointment_datetime: date}, {where:{'patient_id': patient_id, 'dentist_id': dentist_id}})
                            .then(() =>{
                                Appointment.findOne({where:{'patient_id': patient_id, 'dentist_id': dentist_id}}).then(marcacao =>{
                                    res.status(200).send(marcacao);
                                })
                            })
                        }
                    })
                }
            })
        }
    })
}

exports.getAppointmentsOfPatient = (req, res, next)=>{
    const id = req.query.patientId

    Patient.findByPk(id).then(result=>{
        if( result == null) {
            res.status(404).send("O paciente com o ID: " + id + " não existe!")
        } else {
            Appointment.findAll({where: {patient_id: id}}).then(result =>{
                if ( result == null ) {
                    res.status(404).send("O paciente ainda não tem nenhuma marcação!")
                } else res.status(200).send(result)
            })
        }
    })
}

exports.downloadLog = (req, res, next) =>{
    const file = 'log.txt';
    const ruta = './' + file;

    res.download(ruta, file);
}