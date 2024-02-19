const { Course, Student, Grade } = require('../sequelize');

exports.getAllGrades = (req, res, next) =>{
    Grade.findAll({include:[Course, Student]}).then(results =>{
        if (results == null) {
            res.status(404).send('Não existe nenhuma grade registada!')
        }
        else res.status(200).send(results);
    })
}

exports.createGrade = (req, res, next) => {
    const { student_id, course_id, avaliacao } = req.body;

    if (student_id == '' || course_id == '' || avaliacao == '') {
        res.status(400).send('Preencha todos os campos no body');
    } 
    else {
        Student.findByPk(student_id).then( student => {
            if (student == null) {
                res.status(404).send('O estudante selecionado não existe')
            } 
            else {
                Course.findByPk(course_id).then( course =>{
                    if ( course == null) {
                        res.status(404).send('O curso selecionado não existe')
                    }
                    else {
                        Grade.create({'student_id': student_id, 'course_id': course_id, 'grade': avaliacao }).then(grade =>{
                            res.status(200).send('O estudante com o ID: ' + student_id + ' tive uma nota de ' + avaliacao + ' no curso com o ID: ' + course_id)
                        })
                    }
                })
            }
        })
    }
}

exports.deleteGrade = (req,res,next)=>{
    var id = req.query.id;

    Grade.findByPk(id).then(grade =>{
        if ( grade == null ) {
            res.status(404).send('Não existe nenhum grade com o ID selecionado!');
        } else {
            Grade.destroy({where:{grade_id: id}}).then(rowCount =>{
                res.status(200).send('O grade com o ID: ' + id + ' foi eliminado com successo e o numero de linhas afetadas foi: ' +rowCount);
            })
        }
    })
}

exports.updateGrade = (req, res, next) =>{
    const student_id = req.params.student_id;
    const course_id = req.params.course_id;
    const { avaliacao } = req.body;

    if ( avaliacao == '') {
        res.status(400).send('Preencha todos os campos no body');
    } 
    else {
        Student.findByPk(student_id).then( student => {
            if (student == null) {
                res.status(404).send('O estudante selecionado não existe')
            } 
            else {
                Course.findByPk(course_id).then( course =>{
                    if ( course == null) {
                        res.status(404).send('O curso selecionado não existe')
                    }
                    else {
                        Grade.update({'grade': avaliacao }, {where: {'student_id': student_id, 'course_id': course_id}}).then(() =>{
                                Grade.findOne({where: {'student_id': student_id, 'course_id': course_id}}).then( grade =>{
                                    res.status(200).send(grade);
                                })
                        })
                    }
                })
            }
        })
    }
}

exports.getAllGradesForOneStudent = (req, res, next) =>{
    const student_id = req.params.student_id;

    Student.findByPk(student_id).then(student =>{
        if ( student == null) {
            res.status(404).send('O estudante selecionado não existe!')
        } else {
            Grade.findAll({where:{'student_id': student_id}}).then( grade => {
                if ( grade == null ) {
                    res.status(404).send('O estudante selecionado não tem nenhuma nota associada!')
                } else res.status(200).send(grade)
            })
        }
    })
}