function wrap_project


python_package_name = 'fieldtrip'; 
matlab_project_url  = 'https://github.com/fieldtrip/fieldtrip.git'; 
[~, matlab_project_name] = fileparts(matlab_project_url); 
mpython_url = 'https://github.com/MPython-Package-Factory/mpython.git';

[cpath, ~, ~] = fileparts(mfilename('fullpath'));
python_package_path = fullfile(cpath, '..'); 

restoredefaultpath; 

cd(cpath);

mkdir('external');
cd('external');

if ~exist(matlab_project_name, 'dir')
    system(sprintf('git clone --depth=1 %s', matlab_project_url)); 
else 
    system(sprintf('git -C %s pull', matlab_project_name));
end

if ~exist('mpython', 'dir')
    system(sprintf('git clone --depth=1 %s', mpython_url));
else 
    system('git -C mpython pull');
end

cd('..'); 

addpath(fullfile(cpath, 'external', 'mpython'));
addpath(fullfile(cpath, 'external', matlab_project_name));

mkdir('build'); 
srcpath   = fullfile('external', matlab_project_name);
buildpath = fullfile('build', matlab_project_name); 
copyfile(srcpath, buildpath); 

ignored = {
    '.git'
    '.github'
    'test'
    'external'
    'compat'
};
for i = 1:length(ignored)
    try
        rmdir(fullfile(buildpath, ignored{i}), 's');
        fprintf('Removed %s\n', fullfile(buildpath, ignored{i}));
    catch e
        warning(e.message);
        fprintf('Could not remove %s\n', fullfile(buildpath, ignored{i}));
    end
    try
        delete(fullfile(buildpath, ignored{i}));
        fprintf('Deleted %s\n', fullfile(buildpath, ignored{i}));
    catch e
        warning(e.message);
        fprintf('Could not remove %s\n', fullfile(buildpath, ignored{i}));
    end
end


toolboxes = {
    'signal'
    'stats'
    'newunits'
    'syms'
    'images'
    'parfor'
};
mpython_compile(buildpath, python_package_path, python_package_name, toolboxes)


mpython_wrap( ...
    buildpath, ...
    python_package_path, ...
    python_package_name, ...
    true, ...
    fullfile(cpath, 'templates'))

end
