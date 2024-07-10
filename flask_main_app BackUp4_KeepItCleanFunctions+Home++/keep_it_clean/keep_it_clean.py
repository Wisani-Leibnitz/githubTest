from flask import render_template, request, redirect, url_for, flash, session
from . import keep_it_clean_bp
from models import db, Report  # Ensure the Report model is imported correctly

@keep_it_clean_bp.route('/', methods=['GET', 'POST'])
def index():
    """Render the keep it clean index page with form and table."""
    errors = {}
    form_data = {}

    if request.method == 'POST':
        description = request.form.get('description', '').strip()
        image_path = request.form.get('image_path', '').strip()
        geo_location = request.form.get('geo_location', '').strip()
        
        # Validate inputs
        if not description:
            errors['description'] = 'Description is required.'
        if not image_path:
            errors['image_path'] = 'Image Path is required.'
        if not geo_location:
            errors['geo_location'] = 'Geo Location is required.'

        form_data = request.form.to_dict()

        if not errors:
            # Manually increment the ID
            last_report = Report.query.order_by(Report.id.desc()).first()
            new_id = last_report.id + 1 if last_report else 1

            new_report = Report(
                id=new_id,  # Set the new ID
                user_id=session['user_id'],
                description=description,
                image_path=image_path,
                geo_location=geo_location
            )
            db.session.add(new_report)
            db.session.commit()
            flash('Report added successfully!', 'success')
            return redirect(url_for('keep_it_clean.index'))

    reports = Report.query.all()
    return render_template('keep_it_clean.html', reports=reports, errors=errors, form_data=form_data)
